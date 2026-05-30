# Decision Report

- generated_at: 2026-05-30T14:00:00.499999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5128**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=5128, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.33% | **+1.20%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.84% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.86% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.04% | **+1.22%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.35% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.25** / 初期 $100.00 (+25.25%)
- 確定: 783件 (Win 183 / Loss 238 / Flat 362) / skip 906件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.91%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $125.25

## 4. Latest Market Context

- 更新: 2026-05-30T13:59:52.860621+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=73801.7
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 82.1 >= 65=1, 4h RSI 69.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +55.52% | $3,388,589.69 |
| NFP/USDT:USDT | +37.48% | $3,616,218.91 |
| LAB/USDT:USDT | +36.77% | $141,766,058.68 |
| STG/USDT:USDT | +31.02% | $1,996,219.19 |
| H/USDT:USDT | +28.90% | $6,431,936.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.49% | +4.30% |
| PORTAL/USDT:USDT | below_1h_threshold | +3.81% | +3.62% |
| BEAT/USDT:USDT | below_1h_threshold | +3.52% | +3.33% |
| BASED/USDT:USDT | below_1h_threshold | +3.05% | +2.86% |
| LAB/USDT:USDT | below_1h_threshold | +2.72% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
