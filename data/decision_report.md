# Decision Report

- generated_at: 2026-08-26T09:16:25.918596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12688**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12688, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -1.04% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.67% | **+2.13%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.36% | **+2.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.48% | **+1.91%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.28% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$701.35** / 初期 $100.00 (+601.35%)
- 確定: 4590件 (Win 1396 / Loss 1507 / Flat 1687) / skip 4659件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $701.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.23** / 初期 $100.00 (+58.23%)
- 確定: 1985件 (Win 540 / Loss 474 / Flat 971) / skip 4114件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0480 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $158.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.63** / 初期 $100.00 (+16.63%)
- 確定: 1964件 (Win 577 / Loss 748 / Flat 639) / pending 6件 / skip 2194件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000449 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.63

## 6. Latest Market Context

- 更新: 2026-08-26T09:16:15.996754+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78684.7
- Funnel: target 1018 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +171.41% | $12,345,915.45 |
| BMT/USDT:USDT | +50.34% | $13,627,724.28 |
| TAC/USDT:USDT | +47.78% | $5,098,232.32 |
| LONGXIA/USDT:USDT | +34.58% | $1,947,060.38 |
| PORTAL/USDT:USDT | +24.72% | $3,842,925.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.67% | +2.66% |
| ONG/USDT:USDT | below_1h_threshold | +1.62% | +1.61% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.26% | +1.25% |
| BR/USDT:USDT | below_1h_threshold | +1.13% | +1.12% |
| BICO/USDT:USDT | below_1h_threshold | +1.04% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
