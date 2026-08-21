# Decision Report

- generated_at: 2026-08-21T03:41:41.582152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12140**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12140, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.21% | **-1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.79% | **+0.62%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.03% | **+2.21%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.62% | **+1.31%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.04% | **+1.21%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.05% | **+1.02%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$657.01** / 初期 $100.00 (+557.01%)
- 確定: 4351件 (Win 1337 / Loss 1428 / Flat 1586) / skip 4350件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.06% 残高後 $657.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3729件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0573 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.41** / 初期 $100.00 (+17.41%)
- 確定: 1821件 (Win 540 / Loss 690 / Flat 591) / pending 3件 / skip 1792件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.41

## 6. Latest Market Context

- 更新: 2026-08-21T03:41:23.605306+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=74530.0
- Funnel: target 1011 → liquid 194 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1, 4h RSI 75.7 >= 65=1, 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +123.70% | $4,788,348.32 |
| ONG/USDT:USDT | +92.22% | $33,830,974.85 |
| BTW/USDT:USDT | +24.51% | $88,256,333.24 |
| ONT/USDT:USDT | +23.58% | $3,695,991.85 |
| ENA/USDT:USDT | +22.67% | $55,834,333.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +4.03% | +3.87% |
| TUT/USDT:USDT | below_1h_threshold | +2.54% | +2.38% |
| GRASS/USDT:USDT | below_1h_threshold | +2.44% | +2.28% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.31% | +2.15% |
| CHIP/USDT:USDT | below_1h_threshold | +2.14% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
