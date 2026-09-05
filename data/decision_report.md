# Decision Report

- generated_at: 2026-09-05T13:41:22.480666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13735**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13735, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.59% | **+0.47%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.78% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$853.17** / 初期 $100.00 (+753.17%)
- 確定: 5041件 (Win 1518 / Loss 1648 / Flat 1875) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $853.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.40** / 初期 $100.00 (+88.40%)
- 確定: 2480件 (Win 696 / Loss 587 / Flat 1197) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0742 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.92** / 初期 $100.00 (+18.92%)
- 確定: 2360件 (Win 703 / Loss 901 / Flat 756) / pending 5件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.92

## 6. Latest Market Context

- 更新: 2026-09-05T13:41:12.239119+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=79666.6
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +77.99% | $15,027,662.62 |
| 4/USDT:USDT | +63.88% | $21,093,548.24 |
| AKE/USDT:USDT | +43.35% | $18,192,001.57 |
| BASECAT/USDT:USDT | +39.52% | $1,831,931.88 |
| ICX/USDT:USDT | +36.18% | $1,091,278.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +4.70% | +4.70% |
| TUT/USDT:USDT | below_1h_threshold | +2.94% | +2.94% |
| PONS/USDT:USDT | below_1h_threshold | +1.57% | +1.57% |
| ASTER/USDT:USDT | below_1h_threshold | +1.52% | +1.52% |
| 4/USDT:USDT | below_1h_threshold | +1.27% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
