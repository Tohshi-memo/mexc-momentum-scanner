# Decision Report

- generated_at: 2026-07-02T13:52:03.600548+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8085**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=8085, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.52% | **+0.61%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.52% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.25% | **+0.17%** |
| ASK_LONG | 20/20 | 100.0% | +0.03% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2202件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 940件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T13:51:56.875608+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.63% price=61896.3
- Funnel: target 834 → liquid 176 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1, 4h RSI 72.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +82.17% | $15,853,319.07 |
| BIRB/USDT:USDT | +72.35% | $8,620,007.96 |
| M/USDT:USDT | +41.22% | $6,094,161.90 |
| US/USDT:USDT | +33.01% | $2,145,097.53 |
| BREV/USDT:USDT | +30.41% | $6,066,330.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WENSTOCK/USDT:USDT | below_1h_threshold | +4.52% | +3.89% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +4.02% | +3.39% |
| M/USDT:USDT | below_1h_threshold | +3.73% | +3.10% |
| ETH/USDT:USDT | below_1h_threshold | +2.95% | +2.32% |
| BIRB/USDT:USDT | below_1h_threshold | +2.95% | +2.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
