# Decision Report

- generated_at: 2026-05-30T12:09:47.100460+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5122**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.71% / filled 20/20。**
- 全期間 MARKET基準: n=5122, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.71% | **+1.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.77% | **+1.77%** |
| MARKET | 20/20 | 100.0% | +1.71% | **+1.71%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.60% | **+1.36%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.62% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.34% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.29% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.01** / 初期 $100.00 (+26.01%)
- 確定: 777件 (Win 182 / Loss 235 / Flat 360) / skip 906件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $126.01

## 4. Latest Market Context

- 更新: 2026-05-30T12:09:44.657664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=73565.6
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +37.84% | $1,813,552.08 |
| LAB/USDT:USDT | +30.49% | $120,187,031.77 |
| NFP/USDT:USDT | +29.73% | $3,221,421.25 |
| H/USDT:USDT | +24.10% | $4,587,403.69 |
| HEI/USDT:USDT | +21.03% | $18,687,536.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNTSTOCK/USDT:USDT | below_1h_threshold | +2.05% | +2.05% |
| HEI/USDT:USDT | below_1h_threshold | +1.63% | +1.64% |
| ID/USDT:USDT | below_1h_threshold | +1.54% | +1.55% |
| BEAT/USDT:USDT | below_1h_threshold | +0.91% | +0.91% |
| HBAR/USDT:USDT | below_1h_threshold | +0.81% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
