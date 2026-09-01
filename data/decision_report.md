# Decision Report

- generated_at: 2026-09-01T19:46:32.902501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13265**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13265, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.51% | **-1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.96% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.00% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.22% | **+1.89%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$817.36** / 初期 $100.00 (+717.36%)
- 確定: 4900件 (Win 1493 / Loss 1614 / Flat 1793) / skip 4926件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272` TP_HIT account +1.00% 残高後 $817.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.91** / 初期 $100.00 (+75.91%)
- 確定: 2244件 (Win 628 / Loss 539 / Flat 1077) / skip 4432件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0287 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $175.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T19:46:18.615586+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=77291.1
- Funnel: target 1036 → liquid 164 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +15.77% | $2,099,051.82 |
| ACE/USDT:USDT | +12.38% | $6,263,103.21 |
| FILECOIN/USDT:USDT | +11.02% | $15,092,539.09 |
| USELESS/USDT:USDT | +10.88% | $37,067,929.44 |
| FONE/USDT:USDT | +9.53% | $1,138,426.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +3.27% | +3.04% |
| CRV/USDT:USDT | below_1h_threshold | +2.45% | +2.23% |
| FLOCK/USDT:USDT | below_1h_threshold | +2.11% | +1.89% |
| SPX/USDT:USDT | below_1h_threshold | +1.99% | +1.76% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.89% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
