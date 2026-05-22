# Decision Report

- generated_at: 2026-05-22T04:54:03.682805+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4665**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.37% / filled 20/20。**
- 全期間 MARKET基準: n=4665, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.72% | **+1.37%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.42% | **+1.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.75% | **+1.88%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | -0.08% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 678件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T04:54:01.085392+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77648.0
- Funnel: target 766 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +87.48% | $1,522,614.22 |
| NEAR/USDT:USDT | +19.54% | $60,490,547.74 |
| GRASS/USDT:USDT | +15.10% | $3,943,768.15 |
| IBMSTOCK/USDT:USDT | +8.82% | $2,473,370.72 |
| PLUME/USDT:USDT | +8.21% | $1,767,813.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.40% | +3.52% |
| RAVE/USDT:USDT | below_1h_threshold | +2.78% | +2.90% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.60% | +2.72% |
| LIT/USDT:USDT | below_1h_threshold | +2.54% | +2.66% |
| NEAR/USDT:USDT | below_1h_threshold | +1.94% | +2.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
