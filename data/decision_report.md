# Decision Report

- generated_at: 2026-06-18T20:54:29.786407+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7077**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7077, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.48% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.06% | **-0.03%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.04% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.76% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.08% | **+0.70%** |
| ASK_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.48** / 初期 $100.00 (+2.48%)
- 確定トレード: 16件 (TP 7 / SL 9 / EXP 0)
- 最新: FOLKS/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.48
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.45** / 初期 $100.00 (+124.45%)
- 確定: 1897件 (Win 540 / Loss 606 / Flat 751) / skip 1741件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEREBRO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $224.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 180件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T20:54:24.829288+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=63087.7
- Funnel: target 795 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1, 4h RSI 70.1 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +24.84% | $19,053,357.02 |
| ZEREBRO/USDT:USDT | +21.62% | $2,274,623.83 |
| BASED/USDT:USDT | +16.73% | $1,673,680.89 |
| PLAY/USDT:USDT | +14.28% | $1,904,872.01 |
| EDEN/USDT:USDT | +13.93% | $1,451,752.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_relative_strength | +5.25% | +4.99% |
| CHIP/USDT:USDT | below_1h_threshold | +4.43% | +4.17% |
| DYDX/USDT:USDT | below_1h_threshold | +4.34% | +4.09% |
| EDEN/USDT:USDT | below_1h_threshold | +2.89% | +2.63% |
| WLD/USDT:USDT | below_1h_threshold | +2.87% | +2.61% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
