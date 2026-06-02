# Decision Report

- generated_at: 2026-06-02T00:38:51.380338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5381**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=5381, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.59% | **+1.59%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.06% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.10% | **+0.77%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.50% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.10% | **+0.04%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.40% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 898件 (Win 208 / Loss 270 / Flat 420) / skip 1044件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-02T00:38:48.611987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=71253.6
- Funnel: target 774 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +66.42% | $8,250,785.63 |
| MYX/USDT:USDT | +13.44% | $6,688,757.03 |
| UB/USDT:USDT | +12.18% | $2,422,896.44 |
| WLD/USDT:USDT | +12.00% | $138,841,751.08 |
| ORDI/USDT:USDT | +10.43% | $6,515,060.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.08% | +4.27% |
| LAB/USDT:USDT | below_1h_threshold | +3.17% | +3.36% |
| H/USDT:USDT | below_1h_threshold | +2.80% | +3.00% |
| CHZ/USDT:USDT | below_1h_threshold | +2.47% | +2.66% |
| NEX/USDT:USDT | below_1h_threshold | +2.18% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
