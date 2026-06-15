# Decision Report

- generated_at: 2026-06-15T05:50:16.273478+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6748**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6748, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| ASK | 20/20 | 100.0% | +0.21% | **+0.21%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.95% | **+1.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_BB3S_LONG | 4/11 | 36.4% | +1.42% | **+0.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.88** / 初期 $100.00 (+73.88%)
- 確定: 1621件 (Win 424 / Loss 503 / Flat 694) / skip 1688件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $173.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定: 115件 (Win 24 / Loss 19 / Flat 72) / skip 44件
- 成長率目線: 平均log -0.000044 / 幾何平均 -0.004% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0412 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $99.49

## 5. Latest Market Context

- 更新: 2026-06-15T05:50:09.882038+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=65730.5
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +107.51% | $3,151,653.68 |
| EVAA/USDT:USDT | +70.13% | $20,418,981.65 |
| CLO/USDT:USDT | +37.08% | $2,135,059.83 |
| GRASS/USDT:USDT | +20.79% | $1,454,591.97 |
| WLD/USDT:USDT | +17.42% | $110,109,957.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.85% | +3.67% |
| CHIP/USDT:USDT | below_1h_threshold | +3.32% | +3.14% |
| ENA/USDT:USDT | below_1h_threshold | +2.69% | +2.51% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.40% | +2.22% |
| NIL/USDT:USDT | below_1h_threshold | +2.26% | +2.08% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
