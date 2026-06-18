# Decision Report

- generated_at: 2026-06-18T01:02:12.922610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6989**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6989, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.15% | **-1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.44% | **+0.15%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |
| LIMIT_ATR | 11/20 | 55.0% | -0.73% | **-0.40%** |
| LIMIT_8PCT | 7/20 | 35.0% | -1.19% | **-0.41%** |
| LIMIT_5PCT | 9/20 | 45.0% | -1.57% | **-0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +2.00% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$207.78** / 初期 $100.00 (+107.78%)
- 確定: 1836件 (Win 506 / Loss 579 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $207.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.62** / 初期 $100.00 (+4.62%)
- 確定: 262件 (Win 71 / Loss 67 / Flat 124) / skip 138件
- 成長率目線: 平均log +0.000172 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0825 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $104.62

## 5. Latest Market Context

- 更新: 2026-06-18T01:02:06.941090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=64515.2
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +158.77% | $25,696,229.37 |
| O/USDT:USDT | +76.08% | $1,508,317.97 |
| SYN/USDT:USDT | +38.87% | $4,323,762.30 |
| H/USDT:USDT | +18.78% | $38,561,664.77 |
| MITO/USDT:USDT | +13.74% | $1,704,357.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +0.99% | +0.86% |
| MITO/USDT:USDT | below_1h_threshold | +0.60% | +0.47% |
| PLAY/USDT:USDT | below_1h_threshold | +0.58% | +0.46% |
| XLM/USDT:USDT | below_1h_threshold | +0.56% | +0.44% |
| RAVE/USDT:USDT | below_1h_threshold | +0.55% | +0.42% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
