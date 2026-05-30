# Decision Report

- generated_at: 2026-05-30T12:19:43.600011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5123**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.31% / filled 20/20。**
- 全期間 MARKET基準: n=5123, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.31% | **+2.31%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.25% | **+1.91%** |
| ASK | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_BB3S | 5/16 | 31.2% | +1.81% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.09% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.38** / 初期 $100.00 (+25.38%)
- 確定: 778件 (Win 182 / Loss 236 / Flat 360) / skip 906件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.72%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $125.38

## 4. Latest Market Context

- 更新: 2026-05-30T12:19:40.848212+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=73608.6
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +38.49% | $1,975,705.24 |
| NFP/USDT:USDT | +28.27% | $3,246,245.69 |
| LAB/USDT:USDT | +28.07% | $121,785,928.91 |
| VTHO/USDT:USDT | +21.00% | $1,725,333.55 |
| HEI/USDT:USDT | +19.83% | $18,783,010.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNTSTOCK/USDT:USDT | below_1h_threshold | +3.10% | +3.04% |
| ID/USDT:USDT | below_1h_threshold | +1.94% | +1.88% |
| BEAT/USDT:USDT | below_1h_threshold | +1.24% | +1.18% |
| VTHO/USDT:USDT | below_1h_threshold | +1.01% | +0.95% |
| FET/USDT:USDT | below_1h_threshold | +1.00% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
