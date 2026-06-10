# Decision Report

- generated_at: 2026-06-10T22:51:18.707030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6276**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6276, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +0.75% | **+0.49%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.01% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.20** / 初期 $100.00 (+51.20%)
- 確定: 1262件 (Win 318 / Loss 395 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $151.20

## 4. Latest Market Context

- 更新: 2026-06-10T22:51:15.311160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=61415.1
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1, 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +90.63% | $35,891,387.57 |
| BEAT/USDT:USDT | +27.62% | $179,115,925.81 |
| STRAX/USDT:USDT | +13.71% | $1,258,238.30 |
| FOLKS/USDT:USDT | +7.10% | $12,135,933.48 |
| STG/USDT:USDT | +5.59% | $23,175,348.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +3.06% | +2.92% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.76% | +2.62% |
| ALLO/USDT:USDT | below_1h_threshold | +2.37% | +2.23% |
| KITE/USDT:USDT | below_1h_threshold | +1.32% | +1.17% |
| MYX/USDT:USDT | below_1h_threshold | +1.13% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
