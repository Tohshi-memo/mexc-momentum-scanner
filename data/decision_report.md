# Decision Report

- generated_at: 2026-08-21T07:56:30.746582+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12161**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12161, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.18% | **+0.35%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.84% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +6.78% | **+4.52%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.96% | **+1.18%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.04%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4361件 (Win 1337 / Loss 1434 / Flat 1590) / skip 4361件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1823件 (Win 502 / Loss 429 / Flat 892) / skip 3749件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0412 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.21** / 初期 $100.00 (+17.21%)
- 確定: 1822件 (Win 540 / Loss 691 / Flat 591) / pending 2件 / skip 1812件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000193 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.21

## 6. Latest Market Context

- 更新: 2026-08-21T07:56:19.238647+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.98% price=76351.9
- Funnel: target 1015 → liquid 194 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=40, below_relative_strength=4, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 75.7 >= 65=1, 4h RSI 78.1 >= 65=1, 4h RSI 88.2 >= 65=1, 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +104.13% | $5,792,848.56 |
| ONG/USDT:USDT | +37.72% | $42,639,684.08 |
| ENA/USDT:USDT | +29.22% | $80,326,365.55 |
| NIULAI/USDT:USDT | +27.10% | $7,087,579.21 |
| NEIROCTO/USDT:USDT | +25.09% | $3,585,755.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GALA/USDT:USDT | below_relative_strength | +5.95% | +4.98% |
| LINK/USDT:USDT | below_relative_strength | +5.42% | +4.45% |
| PROM/USDT:USDT | below_relative_strength | +5.37% | +4.39% |
| 1000BONK/USDT:USDT | below_relative_strength | +5.04% | +4.06% |
| BRETT/USDT:USDT | below_1h_threshold | +4.60% | +3.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
