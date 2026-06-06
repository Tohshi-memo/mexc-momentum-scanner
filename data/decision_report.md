# Decision Report

- generated_at: 2026-06-06T03:59:16.466225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5778**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5778, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.33% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 2/18 | 11.1% | -0.54% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.72% | **+1.20%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.21% | **+0.73%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.34% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T03:59:13.920119+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=60655.9
- Funnel: target 771 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +30.39% | $5,447,302.79 |
| VELVET/USDT:USDT | +24.67% | $2,010,427.09 |
| OPN/USDT:USDT | +21.18% | $23,839,986.88 |
| BTW/USDT:USDT | +18.93% | $32,005,202.57 |
| ALLO/USDT:USDT | +16.60% | $8,375,325.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.01% | +4.44% |
| HOME/USDT:USDT | below_1h_threshold | +3.60% | +4.03% |
| OPN/USDT:USDT | below_1h_threshold | +2.71% | +3.14% |
| BSB/USDT:USDT | below_1h_threshold | +2.05% | +2.49% |
| ZEST/USDT:USDT | below_1h_threshold | +1.59% | +2.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
