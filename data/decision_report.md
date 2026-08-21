# Decision Report

- generated_at: 2026-08-21T08:51:37.217447+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12168**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12168, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.30% | **+0.52%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +6.78% | **+3.39%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.37% | **+1.54%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.03% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4361件 (Win 1337 / Loss 1434 / Flat 1590) / skip 4368件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1823件 (Win 502 / Loss 429 / Flat 892) / skip 3756件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0685 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.21** / 初期 $100.00 (+17.21%)
- 確定: 1822件 (Win 540 / Loss 691 / Flat 591) / pending 2件 / skip 1816件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.21

## 6. Latest Market Context

- 更新: 2026-08-21T08:51:23.982019+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.46% price=78186.6
- Funnel: target 1014 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=4, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +113.02% | $6,265,247.79 |
| ENA/USDT:USDT | +37.05% | $91,168,361.87 |
| PEOPLE/USDT:USDT | +36.02% | $5,045,332.43 |
| NEIROCTO/USDT:USDT | +35.42% | $3,802,649.00 |
| BOME/USDT:USDT | +30.39% | $20,904,357.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEIROCTO/USDT:USDT | below_relative_strength | +7.28% | +4.82% |
| ENA/USDT:USDT | below_relative_strength | +6.69% | +4.23% |
| FET/USDT:USDT | below_relative_strength | +5.93% | +3.47% |
| XRP/USDT:USDT | below_relative_strength | +5.65% | +3.20% |
| TURBO/USDT:USDT | below_1h_threshold | +4.87% | +2.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
