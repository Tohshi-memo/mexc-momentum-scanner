# Decision Report

- generated_at: 2026-09-05T10:16:26.425307+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13724**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13724, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.81% | **+0.61%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.02% | **+1.01%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$854.06** / 初期 $100.00 (+754.06%)
- 確定: 5031件 (Win 1517 / Loss 1646 / Flat 1868) / skip 5254件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $854.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.78** / 初期 $100.00 (+88.78%)
- 確定: 2469件 (Win 695 / Loss 586 / Flat 1188) / skip 4666件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0794 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $188.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.62** / 初期 $100.00 (+18.62%)
- 確定: 2350件 (Win 701 / Loss 901 / Flat 748) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.62

## 6. Latest Market Context

- 更新: 2026-09-05T10:16:14.516578+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79586.6
- Funnel: target 1050 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +100.76% | $11,014,983.52 |
| 4/USDT:USDT | +62.81% | $19,048,509.71 |
| B/USDT:USDT | +44.41% | $2,469,182.44 |
| AKE/USDT:USDT | +38.66% | $15,206,332.89 |
| MARSCOIN/USDT:USDT | +38.18% | $9,122,610.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.39% | +3.40% |
| DASH/USDT:USDT | below_1h_threshold | +1.95% | +1.96% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.94% | +1.95% |
| RIVER/USDT:USDT | below_1h_threshold | +1.05% | +1.06% |
| 4/USDT:USDT | below_1h_threshold | +0.89% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
