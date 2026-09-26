# Decision Report

- generated_at: 2026-09-26T00:16:31.874276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15551**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15551, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.83% | **-0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_BB3S | 3/15 | 20.0% | +3.54% | **+0.71%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.93% | **+0.61%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.10% | **+1.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.68% | **+1.34%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.75% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.41** / 初期 $100.00 (+1098.41%)
- 確定: 5915件 (Win 1744 / Loss 1897 / Flat 2274) / skip 6197件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $1,198.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$255.78** / 初期 $100.00 (+155.78%)
- 確定: 3484件 (Win 954 / Loss 794 / Flat 1736) / skip 5478件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0521 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $255.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.97** / 初期 $100.00 (+18.97%)
- 確定: 3181件 (Win 934 / Loss 1261 / Flat 986) / pending 5件 / skip 3840件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.97

## 6. Latest Market Context

- 更新: 2026-09-26T00:16:15.980750+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=84040.5
- Funnel: target 1067 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +41.35% | $1,224,396.07 |
| BR/USDT:USDT | +18.46% | $9,352,313.28 |
| PHA/USDT:USDT | +15.25% | $25,383,879.88 |
| ONE/USDT:USDT | +14.00% | $7,981,102.01 |
| WLD/USDT:USDT | +11.54% | $65,121,766.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +2.91% | +2.93% |
| BR/USDT:USDT | below_1h_threshold | +2.27% | +2.28% |
| LYN/USDT:USDT | below_1h_threshold | +1.92% | +1.94% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.87% | +1.89% |
| XAI/USDT:USDT | below_1h_threshold | +1.86% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
