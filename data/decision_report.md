# Decision Report

- generated_at: 2026-06-28T15:35:43.947090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7761, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 7/20 | 35.0% | +4.82% | **+1.69%** |
| LIMIT_10PCT | 6/20 | 30.0% | +5.58% | **+1.67%** |
| LIMIT_8PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_BB3S | 10/15 | 66.7% | +0.87% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| ASK_LONG | 20/20 | 100.0% | +2.38% | **+2.38%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.57** / 初期 $100.00 (+160.57%)
- 確定: 2269件 (Win 694 / Loss 760 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANTA/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $260.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 717件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T15:35:34.971546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=60054.0
- Funnel: target 805 → liquid 121 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MANTA/USDT:USDT | +80.40% | $8,398,738.10 |
| ACT/USDT:USDT | +61.04% | $10,146,979.20 |
| S/USDT:USDT | +29.55% | $9,913,584.98 |
| VELVET/USDT:USDT | +26.26% | $227,308,601.75 |
| RAVE/USDT:USDT | +19.45% | $10,937,002.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POWR/USDT:USDT | below_1h_threshold | +4.26% | +4.16% |
| VELVET/USDT:USDT | below_1h_threshold | +2.52% | +2.42% |
| UB/USDT:USDT | below_1h_threshold | +2.50% | +2.40% |
| BAS/USDT:USDT | below_1h_threshold | +1.90% | +1.80% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.46% | +1.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
