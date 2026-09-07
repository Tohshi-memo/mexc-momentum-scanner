# Decision Report

- generated_at: 2026-09-07T23:06:19.962819+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13921**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13921, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.86% | **-2.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.13% | **+0.94%** |
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +4.15% | **+3.53%** |
| MARKET_LONG | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.39% | **+2.41%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.30% | **+1.32%** |
| LIMIT_6PCT_LONG | 3/20 | 15.0% | +5.04% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$958.80** / 初期 $100.00 (+858.80%)
- 確定: 5194件 (Win 1560 / Loss 1685 / Flat 1949) / skip 5288件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $958.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4760件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0494 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.17** / 初期 $100.00 (+22.17%)
- 確定: 2511件 (Win 741 / Loss 941 / Flat 829) / pending 6件 / skip 2877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $122.17

## 6. Latest Market Context

- 更新: 2026-09-07T23:06:07.940448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78927.7
- Funnel: target 1062 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +65.50% | $6,056,577.64 |
| BONER/USDT:USDT | +26.63% | $4,946,283.82 |
| SOPH/USDT:USDT | +15.38% | $1,746,455.98 |
| AERO/USDT:USDT | +9.60% | $3,691,410.72 |
| PENDLE/USDT:USDT | +7.22% | $1,634,835.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.53% | +1.51% |
| WLD/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| XLM/USDT:USDT | below_1h_threshold | +0.93% | +0.91% |
| USELESS/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |
| AKE/USDT:USDT | below_1h_threshold | +0.71% | +0.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
