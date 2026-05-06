# Decision Report

- generated_at: 2026-05-06T13:12:36.460531+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3460**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3460, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.88% | **+0.69%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.39% | **+0.66%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.88% | **+0.47%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.21% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.10% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 12件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T13:12:33.957599+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=82104.0
- Funnel: target 770 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +93.28% | $2,495,338.99 |
| TONCOIN/USDT:USDT | +35.25% | $222,809,824.21 |
| IO/USDT:USDT | +34.94% | $14,495,026.59 |
| ZEC/USDT:USDT | +34.07% | $764,703,547.87 |
| FHE/USDT:USDT | +33.21% | $32,317,518.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +1.10% | +1.21% |
| IO/USDT:USDT | below_1h_threshold | +1.08% | +1.19% |
| M/USDT:USDT | below_1h_threshold | +0.61% | +0.71% |
| JTO/USDT:USDT | below_1h_threshold | +0.60% | +0.70% |
| SWARMS/USDT:USDT | below_1h_threshold | +0.36% | +0.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
