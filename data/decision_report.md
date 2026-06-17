# Decision Report

- generated_at: 2026-06-17T09:18:03.587350+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6918**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6918, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.98% | **+2.65%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| ASK_LONG | 20/20 | 100.0% | +0.73% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.83** / 初期 $100.00 (+96.83%)
- 確定: 1791件 (Win 485 / Loss 561 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $196.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.25** / 初期 $100.00 (+1.25%)
- 確定: 191件 (Win 43 / Loss 38 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000065 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1097 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $101.25

## 5. Latest Market Context

- 更新: 2026-06-17T09:17:56.185847+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64903.0
- Funnel: target 784 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +38.26% | $5,862,064.91 |
| HIGH/USDT:USDT | +29.61% | $1,735,030.17 |
| SQD/USDT:USDT | +22.86% | $2,604,261.71 |
| ID/USDT:USDT | +20.22% | $1,190,774.73 |
| UNI/USDT:USDT | +17.14% | $55,019,751.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +1.67% | +1.64% |
| UNI/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| SPX/USDT:USDT | below_1h_threshold | +1.53% | +1.51% |
| PLAY/USDT:USDT | below_1h_threshold | +1.51% | +1.49% |
| BTW/USDT:USDT | below_1h_threshold | +1.17% | +1.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
