# Decision Report

- generated_at: 2026-06-18T00:55:16.636326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6987**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6987, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.15% | **-1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.56% | **+0.22%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_8PCT | 8/20 | 40.0% | -0.57% | **-0.23%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |
| LIMIT_7PCT | 8/20 | 40.0% | -1.45% | **-0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.16% | **+3.16%** |
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.00% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$209.87** / 初期 $100.00 (+109.87%)
- 確定: 1834件 (Win 506 / Loss 577 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $209.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.54** / 初期 $100.00 (+4.54%)
- 確定: 260件 (Win 70 / Loss 66 / Flat 124) / skip 138件
- 成長率目線: 平均log +0.000171 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0827 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $104.54

## 5. Latest Market Context

- 更新: 2026-06-18T00:55:07.896744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64500.5
- Funnel: target 790 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +159.77% | $25,256,828.78 |
| O/USDT:USDT | +79.39% | $1,505,625.19 |
| SYN/USDT:USDT | +36.67% | $4,317,555.11 |
| TAC/USDT:USDT | +15.39% | $2,898,886.90 |
| RE/USDT:USDT | +14.38% | $1,857,510.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.73% | +4.70% |
| PLAY/USDT:USDT | below_1h_threshold | +3.99% | +3.96% |
| ID/USDT:USDT | below_1h_threshold | +3.90% | +3.86% |
| FOLKS/USDT:USDT | below_1h_threshold | +3.02% | +2.99% |
| STG/USDT:USDT | below_1h_threshold | +2.97% | +2.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
