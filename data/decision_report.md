# Decision Report

- generated_at: 2026-05-30T11:40:00.551836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5121**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.71% / filled 20/20。**
- 全期間 MARKET基準: n=5121, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.71% | **+1.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| MARKET | 20/20 | 100.0% | +1.71% | **+1.71%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.60% | **+1.36%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.73% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.29% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.01** / 初期 $100.00 (+26.01%)
- 確定: 776件 (Win 182 / Loss 235 / Flat 359) / skip 906件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $126.01

## 4. Latest Market Context

- 更新: 2026-05-30T11:39:58.379358+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=73588.0
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +45.38% | $1,435,397.82 |
| NFP/USDT:USDT | +32.35% | $3,121,193.51 |
| H/USDT:USDT | +28.25% | $3,192,871.52 |
| LAB/USDT:USDT | +27.17% | $127,680,339.01 |
| VTHO/USDT:USDT | +19.50% | $1,563,321.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +3.73% | +3.77% |
| H/USDT:USDT | below_1h_threshold | +3.26% | +3.30% |
| OL/USDT:USDT | below_1h_threshold | +2.90% | +2.94% |
| ID/USDT:USDT | below_1h_threshold | +2.06% | +2.09% |
| DYDX/USDT:USDT | below_1h_threshold | +1.58% | +1.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
