# Decision Report

- generated_at: 2026-07-03T14:13:28.024384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8163**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=8163, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_BB3S | 2/19 | 10.5% | +0.73% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.08% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.89% | **+0.45%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.18% | **+0.10%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.05% | **-0.02%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.13** / 初期 $100.00 (+3.13%)
- 確定トレード: 55件 (TP 20 / SL 34 / EXP 1)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.13
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.55** / 初期 $100.00 (+186.55%)
- 確定: 2484件 (Win 764 / Loss 830 / Flat 890) / skip 2240件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $286.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.19** / 初期 $100.00 (+6.19%)
- 確定: 609件 (Win 147 / Loss 146 / Flat 316) / skip 965件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $106.19

## 5. Latest Market Context

- 更新: 2026-07-03T14:13:22.022538+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=61831.4
- Funnel: target 834 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +44.88% | $3,149,855.32 |
| THE/USDT:USDT | +35.88% | $3,391,351.07 |
| ARPA/USDT:USDT | +32.25% | $6,051,365.33 |
| BLESS/USDT:USDT | +26.71% | $7,241,713.55 |
| RIF/USDT:USDT | +24.69% | $9,835,710.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARPA/USDT:USDT | below_1h_threshold | +2.98% | +3.39% |
| ALLO/USDT:USDT | below_1h_threshold | +2.82% | +3.23% |
| XPL/USDT:USDT | below_1h_threshold | +1.99% | +2.40% |
| BLESS/USDT:USDT | below_1h_threshold | +1.76% | +2.16% |
| RIVER/USDT:USDT | below_1h_threshold | +1.43% | +1.84% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
