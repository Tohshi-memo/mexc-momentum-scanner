# Decision Report

- generated_at: 2026-06-11T19:03:59.661631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6396**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6396, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.78% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.41** / 初期 $100.00 (+53.41%)
- 確定: 1313件 (Win 340 / Loss 418 / Flat 555) / skip 1644件
- 成長率目線: 平均log +0.000326 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $153.41

## 4. Latest Market Context

- 更新: 2026-06-11T19:03:56.814733+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63481.2
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +56.15% | $107,552,925.46 |
| ESPORTS/USDT:USDT | +37.14% | $12,160,877.99 |
| SKYAI/USDT:USDT | +13.39% | $11,774,662.13 |
| SOXL/USDT:USDT | +7.49% | $1,502,384.39 |
| HMSTR/USDT:USDT | +6.78% | $4,274,359.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.27% | +2.19% |
| ENA/USDT:USDT | below_1h_threshold | +1.69% | +1.61% |
| HMSTR/USDT:USDT | below_1h_threshold | +0.87% | +0.79% |
| SPACE/USDT:USDT | below_1h_threshold | +0.61% | +0.53% |
| RAVE/USDT:USDT | below_1h_threshold | +0.60% | +0.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
