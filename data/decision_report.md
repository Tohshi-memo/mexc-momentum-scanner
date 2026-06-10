# Decision Report

- generated_at: 2026-06-10T20:22:59.090285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6259**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6259, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.77% | **+0.27%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.62% | **+0.25%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.86% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.73** / 初期 $100.00 (+49.73%)
- 確定: 1245件 (Win 309 / Loss 387 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $149.73

## 4. Latest Market Context

- 更新: 2026-06-10T20:22:53.087781+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=61827.5
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +56.94% | $25,364,118.95 |
| BEAT/USDT:USDT | +26.89% | $131,523,073.19 |
| JCT/USDT:USDT | +12.21% | $2,175,959.93 |
| STRAX/USDT:USDT | +9.59% | $1,203,205.54 |
| BSB/USDT:USDT | +5.42% | $6,741,096.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.55% | +4.68% |
| VELVET/USDT:USDT | below_1h_threshold | +3.21% | +3.34% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.99% | +3.13% |
| JCT/USDT:USDT | below_1h_threshold | +2.40% | +2.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.34% | +2.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
