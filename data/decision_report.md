# Decision Report

- generated_at: 2026-05-17T22:48:53.795915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4426**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=4426, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.11% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.26% | **+0.89%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.05% | **+0.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.98% | **+0.68%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.66% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定: 423件 (Win 110 / Loss 143 / Flat 170) / skip 564件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.36

## 4. Latest Market Context

- 更新: 2026-05-17T22:48:51.135135+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=77959.1
- Funnel: target 760 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +34.30% | $3,307,445.65 |
| UB/USDT:USDT | +15.73% | $14,288,724.76 |
| BUILDONBOB/USDT:USDT | +10.63% | $1,299,380.13 |
| BILL/USDT:USDT | +7.45% | $34,645,792.87 |
| HYPE/USDT:USDT | +6.18% | $298,634,037.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.28% | +2.80% |
| SILVER/USDT:USDT | below_1h_threshold | +1.69% | +2.21% |
| XPD/USDT:USDT | below_1h_threshold | +1.22% | +1.74% |
| SPACE/USDT:USDT | below_1h_threshold | +1.17% | +1.69% |
| USOIL/USDT:USDT | below_1h_threshold | +0.81% | +1.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
