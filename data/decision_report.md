# Decision Report

- generated_at: 2026-09-05T12:01:19.692097+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13729**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=13729, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.30% | **+1.38%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.67% | **+1.34%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.21% | **+1.33%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.74% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$849.79** / 初期 $100.00 (+749.79%)
- 確定: 5035件 (Win 1517 / Loss 1647 / Flat 1871) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRIA/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $849.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.12** / 初期 $100.00 (+88.12%)
- 確定: 2474件 (Win 695 / Loss 587 / Flat 1192) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $188.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.78** / 初期 $100.00 (+18.78%)
- 確定: 2354件 (Win 702 / Loss 901 / Flat 751) / pending 3件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRIA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $118.78

## 6. Latest Market Context

- 更新: 2026-09-05T12:01:08.020287+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79585.0
- Funnel: target 1050 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +74.72% | $13,457,163.80 |
| 4/USDT:USDT | +54.27% | $20,019,584.60 |
| AKE/USDT:USDT | +44.38% | $16,219,984.71 |
| B/USDT:USDT | +38.87% | $2,981,477.59 |
| NIULAI/USDT:USDT | +37.04% | $1,632,349.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +0.76% | +0.75% |
| SNXX/USDT:USDT | below_1h_threshold | +0.74% | +0.73% |
| PONS/USDT:USDT | below_1h_threshold | +0.59% | +0.58% |
| ASTER/USDT:USDT | below_1h_threshold | +0.58% | +0.57% |
| BULLA/USDT:USDT | below_1h_threshold | +0.38% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
