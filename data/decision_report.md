# Decision Report

- generated_at: 2026-07-08T19:48:11.685638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8502**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8502, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.27% | **+0.57%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_BB3S | 4/19 | 21.1% | +2.15% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.23% | **+0.08%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.13% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$104.10** / 初期 $100.00 (+4.10%)
- 確定トレード: 80件 (TP 29 / SL 50 / EXP 1)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.38** / 初期 $100.00 (+222.38%)
- 確定: 2692件 (Win 852 / Loss 901 / Flat 939) / skip 2371件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $322.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1271件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T19:48:05.077369+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=62194.7
- Funnel: target 851 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +55.42% | $2,055,581.99 |
| POWER/USDT:USDT | +21.47% | $4,698,981.45 |
| VANRY/USDT:USDT | +14.45% | $6,560,209.46 |
| BTW/USDT:USDT | +13.72% | $1,222,936.63 |
| KORU/USDT:USDT | +11.12% | $7,238,450.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.84% | +4.78% |
| TAG/USDT:USDT | below_1h_threshold | +4.62% | +4.57% |
| BTW/USDT:USDT | below_1h_threshold | +3.78% | +3.73% |
| VANRY/USDT:USDT | below_1h_threshold | +3.18% | +3.12% |
| FLNCSTOCK/USDT:USDT | below_1h_threshold | +3.04% | +2.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
