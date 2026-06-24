# Decision Report

- generated_at: 2026-06-24T19:07:54.171643+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7491**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=7491, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.61% | **+2.61%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.03% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -3.56% | **-0.53%** |
| ASK_LONG | 20/20 | 100.0% | -0.75% | **-0.75%** |

## 2. $100 Live Portfolio

- 残高: **$102.44** / 初期 $100.00 (+2.44%)
- 確定トレード: 34件 (TP 13 / SL 21 / EXP 0)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.44
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1931件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 347件 (Win 98 / Loss 95 / Flat 154) / skip 555件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0177 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T19:07:48.860805+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=59650.0
- Funnel: target 808 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +29.62% | $15,324,587.59 |
| BSB/USDT:USDT | +6.71% | $6,120,790.01 |
| MAVIA/USDT:USDT | +4.48% | $1,084,573.63 |
| XPL/USDT:USDT | +4.26% | $6,970,605.39 |
| VELVET/USDT:USDT | +3.61% | $5,534,763.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.80% | +4.67% |
| UB/USDT:USDT | below_1h_threshold | +1.12% | +0.99% |
| LIT/USDT:USDT | below_1h_threshold | +1.11% | +0.98% |
| VELVET/USDT:USDT | below_1h_threshold | +1.04% | +0.90% |
| CLO/USDT:USDT | below_1h_threshold | +0.83% | +0.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
