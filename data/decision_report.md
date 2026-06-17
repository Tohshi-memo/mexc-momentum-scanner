# Decision Report

- generated_at: 2026-06-17T09:45:13.154440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6921, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +4.78% | **+2.99%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.06% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.79** / 初期 $100.00 (+98.79%)
- 確定: 1794件 (Win 487 / Loss 562 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HIGH/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $198.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.03** / 初期 $100.00 (+2.03%)
- 確定: 194件 (Win 45 / Loss 39 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000103 / 幾何平均 +0.010% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1352 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HIGH/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $102.03

## 5. Latest Market Context

- 更新: 2026-06-17T09:45:08.439431+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64916.9
- Funnel: target 784 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HIGH/USDT:USDT | +51.11% | $2,193,605.12 |
| ESPORTS/USDT:USDT | +43.16% | $6,067,066.14 |
| SQD/USDT:USDT | +23.75% | $2,698,642.23 |
| ID/USDT:USDT | +21.97% | $1,234,152.17 |
| UNI/USDT:USDT | +19.46% | $56,733,909.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +3.95% | +3.91% |
| TRIA/USDT:USDT | below_1h_threshold | +3.72% | +3.67% |
| UNI/USDT:USDT | below_1h_threshold | +3.71% | +3.66% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.64% | +3.60% |
| ROAM/USDT:USDT | below_1h_threshold | +2.88% | +2.84% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
