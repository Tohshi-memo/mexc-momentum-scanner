# Decision Report

- generated_at: 2026-09-26T00:36:24.290305+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15555**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15555, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.93% | **+0.88%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_BB3S | 2/18 | 11.1% | +4.25% | **+0.47%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.51% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.11% | **+1.44%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.48% | **+0.89%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.43% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.42** / 初期 $100.00 (+1092.42%)
- 確定: 5918件 (Win 1744 / Loss 1898 / Flat 2276) / skip 6198件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RARE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,192.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$255.96** / 初期 $100.00 (+155.96%)
- 確定: 3487件 (Win 955 / Loss 794 / Flat 1738) / skip 5479件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0376 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $255.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.76** / 初期 $100.00 (+18.76%)
- 確定: 3182件 (Win 934 / Loss 1262 / Flat 986) / pending 4件 / skip 3842件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000141 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.76

## 6. Latest Market Context

- 更新: 2026-09-26T00:36:11.710089+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=83807.0
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +46.47% | $1,254,673.26 |
| BR/USDT:USDT | +17.77% | $9,391,639.87 |
| PHA/USDT:USDT | +16.98% | $25,782,587.63 |
| ONE/USDT:USDT | +12.41% | $8,151,642.94 |
| SEI/USDT:USDT | +11.69% | $37,930,414.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +2.19% | +2.48% |
| LYN/USDT:USDT | below_1h_threshold | +1.98% | +2.28% |
| BTW/USDT:USDT | below_1h_threshold | +1.37% | +1.67% |
| BR/USDT:USDT | below_1h_threshold | +1.36% | +1.65% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.11% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
