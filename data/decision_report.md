# Decision Report

- generated_at: 2026-08-20T17:41:31.218943+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12066**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12066, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.76% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +0.54% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$597.96** / 初期 $100.00 (+497.96%)
- 確定: 4279件 (Win 1307 / Loss 1398 / Flat 1574) / skip 4348件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $597.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3655件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.40** / 初期 $100.00 (+16.40%)
- 確定: 1762件 (Win 524 / Loss 674 / Flat 564) / pending 3件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000080 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.40

## 6. Latest Market Context

- 更新: 2026-08-20T17:41:19.553482+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=72785.8
- Funnel: target 1011 → liquid 202 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +32.61% | $1,089,876.95 |
| BEAT/USDT:USDT | +17.39% | $39,043,463.33 |
| PEOPLE/USDT:USDT | +9.59% | $1,732,909.20 |
| ONG/USDT:USDT | +7.86% | $4,500,152.99 |
| ALLO/USDT:USDT | +7.80% | $2,786,172.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +4.29% | +4.31% |
| FET/USDT:USDT | below_1h_threshold | +3.67% | +3.69% |
| XLM/USDT:USDT | below_1h_threshold | +3.59% | +3.61% |
| ENA/USDT:USDT | below_1h_threshold | +3.52% | +3.54% |
| ALLO/USDT:USDT | below_1h_threshold | +3.21% | +3.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
