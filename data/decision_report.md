# Decision Report

- generated_at: 2026-06-07T08:42:45.726406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5933**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5933, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +2.12% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$140.00** / 初期 $100.00 (+40.00%)
- 確定: 1052件 (Win 255 / Loss 323 / Flat 474) / skip 1442件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $140.00

## 4. Latest Market Context

- 更新: 2026-06-07T08:42:42.789164+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62450.2
- Funnel: target 771 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +60.02% | $6,294,892.25 |
| LAB/USDT:USDT | +39.62% | $64,091,650.21 |
| BTW/USDT:USDT | +34.33% | $9,219,510.35 |
| EDEN/USDT:USDT | +32.51% | $3,012,557.31 |
| BSB/USDT:USDT | +31.04% | $6,177,854.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.42% | +4.28% |
| SIREN/USDT:USDT | below_1h_threshold | +3.29% | +3.15% |
| BSB/USDT:USDT | below_1h_threshold | +2.74% | +2.60% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.49% | +2.35% |
| BABY/USDT:USDT | below_1h_threshold | +1.91% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
