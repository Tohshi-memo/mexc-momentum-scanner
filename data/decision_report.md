# Decision Report

- generated_at: 2026-06-10T19:31:44.632985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6251**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6251, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.16% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.12% | **+0.45%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.74** / 初期 $100.00 (+49.74%)
- 確定: 1238件 (Win 308 / Loss 385 / Flat 545) / skip 1574件
- 成長率目線: 平均log +0.000326 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $149.74

## 4. Latest Market Context

- 更新: 2026-06-10T19:31:40.235646+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=61853.6
- Funnel: target 785 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +56.54% | $22,264,435.18 |
| FOLKS/USDT:USDT | +15.53% | $8,535,095.55 |
| BEAT/USDT:USDT | +14.74% | $120,120,709.82 |
| ESPORTS/USDT:USDT | +8.49% | $25,310,036.10 |
| JCT/USDT:USDT | +7.64% | $2,520,617.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.39% | +3.38% |
| JCT/USDT:USDT | below_1h_threshold | +2.82% | +2.81% |
| LAB/USDT:USDT | below_1h_threshold | +1.36% | +1.35% |
| RIVER/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| STRAX/USDT:USDT | below_1h_threshold | +0.85% | +0.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
