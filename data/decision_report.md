# Decision Report

- generated_at: 2026-05-09T01:22:40.622384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3832**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3832, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.73% | **-1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.37% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.48% | **+0.27%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.34% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.30% | **+1.82%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.92% | **+1.34%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.98% | **+1.34%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.96% | **+1.18%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 200件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T01:22:37.407186+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80217.4
- Funnel: target 767 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +26.31% | $6,455,347.80 |
| ICP/USDT:USDT | +19.66% | $230,015,869.37 |
| PLUME/USDT:USDT | +16.74% | $1,043,313.75 |
| CORE/USDT:USDT | +13.97% | $1,743,397.90 |
| AKT/USDT:USDT | +13.96% | $1,692,310.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.61% | +4.58% |
| IP/USDT:USDT | below_1h_threshold | +4.39% | +4.36% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.07% | +2.04% |
| PLUME/USDT:USDT | below_1h_threshold | +2.00% | +1.97% |
| JUP/USDT:USDT | below_1h_threshold | +1.52% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
