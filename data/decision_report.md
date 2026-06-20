# Decision Report

- generated_at: 2026-06-20T17:21:10.553985+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7257**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=7257, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.61% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| ASK | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.92% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.89% | **-0.31%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -1.12% | **-0.45%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.95** / 初期 $100.00 (+133.95%)
- 確定: 1986件 (Win 582 / Loss 646 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $233.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 358件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T17:21:04.807477+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=63886.2
- Funnel: target 796 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +34.41% | $35,147,577.06 |
| VELVET/USDT:USDT | +14.07% | $13,491,638.96 |
| AGT/USDT:USDT | +10.59% | $2,455,290.33 |
| LAB/USDT:USDT | +6.57% | $28,887,700.61 |
| RIF/USDT:USDT | +4.38% | $3,327,025.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.46% | +4.63% |
| LAB/USDT:USDT | below_1h_threshold | +2.59% | +2.76% |
| RIF/USDT:USDT | below_1h_threshold | +2.31% | +2.48% |
| MANA/USDT:USDT | below_1h_threshold | +2.04% | +2.21% |
| MET/USDT:USDT | below_1h_threshold | +1.37% | +1.54% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
