# Decision Report

- generated_at: 2026-06-01T13:47:20.339899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=5321, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.74% | **+0.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.63% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.35% | **+0.34%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.38% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 988件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T13:47:15.010257+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.74% price=71659.1
- Funnel: target 776 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +108.93% | $41,563,225.76 |
| PORTAL/USDT:USDT | +105.76% | $39,285,019.06 |
| SLX/USDT:USDT | +72.39% | $9,098,862.15 |
| LAB/USDT:USDT | +68.27% | $233,847,307.75 |
| VIC/USDT:USDT | +47.61% | $1,450,404.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +3.69% | +4.43% |
| UKOIL/USDT:USDT | below_1h_threshold | +3.37% | +4.11% |
| NEX/USDT:USDT | below_1h_threshold | +2.86% | +3.60% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.46% | +3.20% |
| VRTSTOCK/USDT:USDT | below_1h_threshold | +2.19% | +2.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
