# Decision Report

- generated_at: 2026-06-11T15:30:41.950856+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6370**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6370, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.45% | **+1.47%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.96% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.42** / 初期 $100.00 (+53.42%)
- 確定: 1289件 (Win 331 / Loss 407 / Flat 551) / skip 1642件
- 成長率目線: 平均log +0.000332 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $153.42

## 4. Latest Market Context

- 更新: 2026-06-11T15:30:39.255768+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62718.2
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +98.80% | $30,316,768.26 |
| VELVET/USDT:USDT | +87.80% | $89,669,716.80 |
| AIO/USDT:USDT | +71.46% | $9,212,861.97 |
| BEAT/USDT:USDT | +61.10% | $240,356,659.78 |
| COLLECT/USDT:USDT | +50.47% | $2,438,034.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.48% | +4.45% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.17% | +4.14% |
| H/USDT:USDT | below_1h_threshold | +3.37% | +3.34% |
| ZRO/USDT:USDT | below_1h_threshold | +2.46% | +2.43% |
| AMCSTOCK/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
