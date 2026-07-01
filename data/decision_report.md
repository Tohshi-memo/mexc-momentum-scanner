# Decision Report

- generated_at: 2026-07-01T23:24:08.520395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8033**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8033, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 8/20 | 40.0% | -0.14% | **-0.05%** |
| LIMIT_9PCT | 8/20 | 40.0% | -0.35% | **-0.14%** |
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |
| LIMIT_8PCT | 9/20 | 45.0% | -1.81% | **-0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| ASK_LONG | 20/20 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$293.40** / 初期 $100.00 (+193.40%)
- 確定: 2430件 (Win 750 / Loss 806 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $293.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.51** / 初期 $100.00 (+5.51%)
- 確定: 544件 (Win 136 / Loss 130 / Flat 278) / skip 900件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.19%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.51

## 5. Latest Market Context

- 更新: 2026-07-01T23:24:03.420548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=60170.1
- Funnel: target 825 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +289.60% | $49,530,712.87 |
| TLM/USDT:USDT | +82.94% | $5,642,488.28 |
| NOM/USDT:USDT | +20.12% | $5,702,517.13 |
| LIT/USDT:USDT | +17.73% | $8,952,348.92 |
| COOKIE/USDT:USDT | +15.12% | $1,103,865.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.87% | +5.33% |
| SYN/USDT:USDT | below_1h_threshold | +1.38% | +1.84% |
| BASED/USDT:USDT | below_1h_threshold | +0.91% | +1.37% |
| VELVET/USDT:USDT | below_1h_threshold | +0.85% | +1.31% |
| COOKIE/USDT:USDT | below_1h_threshold | +0.60% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
