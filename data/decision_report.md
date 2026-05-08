# Decision Report

- generated_at: 2026-05-08T23:37:33.843374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3828**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3828, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/16 | 37.5% | +1.59% | **+0.60%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.42% | **+0.29%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.50% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.81% | **+0.49%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.14% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 196件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T23:37:30.584580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80090.6
- Funnel: target 767 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +16.86% | $5,428,086.55 |
| BILL/USDT:USDT | +14.58% | $17,850,998.29 |
| OP/USDT:USDT | +13.62% | $33,747,830.03 |
| CORE/USDT:USDT | +11.93% | $1,660,562.30 |
| ICP/USDT:USDT | +11.10% | $212,398,883.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.34% | +3.52% |
| AKT/USDT:USDT | below_1h_threshold | +2.36% | +2.54% |
| DOGS/USDT:USDT | below_1h_threshold | +1.89% | +2.08% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.71% | +1.90% |
| JASMY/USDT:USDT | below_1h_threshold | +0.99% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
