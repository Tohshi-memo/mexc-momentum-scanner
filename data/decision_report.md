# Decision Report

- generated_at: 2026-06-25T02:52:18.579403+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7515**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7515, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.06% | **+0.26%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.03% | **+0.00%** |
| LIMIT_BB3S | 6/19 | 31.6% | -1.17% | **-0.37%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | -0.57% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.51% | **+2.46%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.98% | **+2.38%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.08% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK_LONG | 20/20 | 100.0% | +1.19% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.68** / 初期 $100.00 (+123.68%)
- 確定: 2123件 (Win 628 / Loss 710 / Flat 785) / skip 1953件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $223.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 576件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T02:52:11.021607+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=60689.3
- Funnel: target 808 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +18.85% | $11,638,128.87 |
| UB/USDT:USDT | +16.42% | $4,720,024.73 |
| KORU/USDT:USDT | +16.09% | $5,873,901.99 |
| MUSTOCK/USDT:USDT | +15.60% | $100,319,630.25 |
| MAVIA/USDT:USDT | +11.92% | $1,511,432.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +2.70% | +3.04% |
| VELVET/USDT:USDT | below_1h_threshold | +2.28% | +2.61% |
| GRASS/USDT:USDT | below_1h_threshold | +2.17% | +2.51% |
| LIT/USDT:USDT | below_1h_threshold | +2.05% | +2.39% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.92% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
