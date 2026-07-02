# Decision Report

- generated_at: 2026-07-02T04:08:05.789454+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8045**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=8045, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |
| LIMIT_1PCT | 16/20 | 80.0% | -0.06% | **-0.05%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.42% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.07% | **+0.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | -0.37% | **-0.09%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.23% | **-0.12%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.37% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$287.54** / 初期 $100.00 (+187.54%)
- 確定: 2442件 (Win 754 / Loss 814 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $287.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 545件 (Win 136 / Loss 131 / Flat 278) / skip 911件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T04:08:00.954261+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=60870.6
- Funnel: target 827 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +229.92% | $77,936,755.51 |
| TLM/USDT:USDT | +43.30% | $7,747,341.67 |
| RIF/USDT:USDT | +24.28% | $4,298,640.72 |
| SLX/USDT:USDT | +19.91% | $8,304,304.48 |
| LIT/USDT:USDT | +17.14% | $10,926,948.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.56% | +2.83% |
| TLM/USDT:USDT | below_1h_threshold | +1.73% | +2.00% |
| BSB/USDT:USDT | below_1h_threshold | +1.50% | +1.77% |
| JTO/USDT:USDT | below_1h_threshold | +1.45% | +1.72% |
| TAIKO/USDT:USDT | below_1h_threshold | +1.44% | +1.70% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
