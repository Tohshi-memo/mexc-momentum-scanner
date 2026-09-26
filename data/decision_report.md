# Decision Report

- generated_at: 2026-09-26T00:26:28.558006+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15552**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15552, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_BB3S | 2/15 | 13.3% | +4.25% | **+0.57%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.50% | **+1.63%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.41** / 初期 $100.00 (+1098.41%)
- 確定: 5916件 (Win 1744 / Loss 1897 / Flat 2275) / skip 6197件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,198.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$255.78** / 初期 $100.00 (+155.78%)
- 確定: 3484件 (Win 954 / Loss 794 / Flat 1736) / skip 5479件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0398 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $255.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.97** / 初期 $100.00 (+18.97%)
- 確定: 3181件 (Win 934 / Loss 1261 / Flat 986) / pending 5件 / skip 3841件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000169 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.97

## 6. Latest Market Context

- 更新: 2026-09-26T00:26:13.055941+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=84009.8
- Funnel: target 1067 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +41.70% | $1,236,713.47 |
| BR/USDT:USDT | +17.75% | $9,383,499.64 |
| PHA/USDT:USDT | +16.70% | $25,591,019.37 |
| ONE/USDT:USDT | +15.60% | $8,072,080.79 |
| SEI/USDT:USDT | +12.51% | $37,766,984.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.85% | +2.91% |
| WLD/USDT:USDT | below_1h_threshold | +2.77% | +2.82% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.10% | +2.16% |
| BTW/USDT:USDT | below_1h_threshold | +1.99% | +2.04% |
| ORDI/USDT:USDT | below_1h_threshold | +1.84% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
