# Decision Report

- generated_at: 2026-06-09T05:39:16.085807+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6117**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6117, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.48% | **+0.31%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.69% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 10件 (TP 1 / SL 8 / EXP 1)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.24** / 初期 $100.00 (+54.24%)
- 確定: 1157件 (Win 288 / Loss 355 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $154.24

## 4. Latest Market Context

- 更新: 2026-06-09T05:39:12.326149+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=63400.0
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +41.60% | $24,577,617.44 |
| ZEST/USDT:USDT | +27.67% | $1,128,313.73 |
| SLX/USDT:USDT | +17.54% | $1,345,089.42 |
| POWER/USDT:USDT | +16.89% | $1,284,141.85 |
| CTR/USDT:USDT | +14.50% | $1,168,057.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_relative_strength | +5.02% | +4.72% |
| BANK/USDT:USDT | below_1h_threshold | +3.94% | +3.65% |
| POWER/USDT:USDT | below_1h_threshold | +3.77% | +3.47% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.52% | +3.22% |
| CTR/USDT:USDT | below_1h_threshold | +3.47% | +3.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
