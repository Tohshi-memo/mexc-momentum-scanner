# Decision Report

- generated_at: 2026-06-15T10:56:44.338320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6773**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6773, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.84% | **+0.21%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 6/17 | 35.3% | -0.03% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.51** / 初期 $100.00 (+74.51%)
- 確定: 1646件 (Win 429 / Loss 510 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $174.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.46** / 初期 $100.00 (-1.54%)
- 確定: 140件 (Win 27 / Loss 25 / Flat 88) / skip 44件
- 成長率目線: 平均log -0.000111 / 幾何平均 -0.011% per trade / maxDD +2.18%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $98.46

## 5. Latest Market Context

- 更新: 2026-06-15T10:56:37.778047+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=65876.0
- Funnel: target 771 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +91.73% | $28,516,094.43 |
| ASTEROID/USDT:USDT | +88.11% | $4,721,068.78 |
| CLO/USDT:USDT | +39.86% | $2,329,620.25 |
| UAI/USDT:USDT | +30.33% | $2,564,932.72 |
| PUFFER/USDT:USDT | +23.10% | $1,490,523.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +4.68% | +4.19% |
| NIL/USDT:USDT | below_1h_threshold | +3.89% | +3.41% |
| INJ/USDT:USDT | below_1h_threshold | +3.72% | +3.24% |
| BCH/USDT:USDT | below_1h_threshold | +3.47% | +2.98% |
| ENA/USDT:USDT | below_1h_threshold | +3.26% | +2.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
