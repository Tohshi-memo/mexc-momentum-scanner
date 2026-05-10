# Decision Report

- generated_at: 2026-05-10T08:12:44.393648+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3952**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3952, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.26% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| ASK_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.41% | **+0.84%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.37% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 316件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T08:12:41.020881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80732.1
- Funnel: target 769 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +68.31% | $1,366,921.03 |
| LAYER/USDT:USDT | +42.90% | $6,096,837.70 |
| XEC/USDT:USDT | +25.79% | $2,033,811.09 |
| SATO/USDT:USDT | +18.80% | $6,219,554.77 |
| BAS/USDT:USDT | +17.22% | $1,182,096.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.74% | +3.69% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.29% | +1.25% |
| SUI/USDT:USDT | below_1h_threshold | +1.21% | +1.16% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.03% | +0.98% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.00% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
