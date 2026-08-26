# Decision Report

- generated_at: 2026-08-26T10:01:22.517358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12693**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12693, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.54%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.30% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.03% | **+1.83%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.19% | **+1.64%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.46% | **+1.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.69** / 初期 $100.00 (+606.69%)
- 確定: 4594件 (Win 1398 / Loss 1508 / Flat 1688) / skip 4660件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $706.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.03** / 初期 $100.00 (+59.03%)
- 確定: 1989件 (Win 542 / Loss 475 / Flat 972) / skip 4115件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1755 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $159.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.73** / 初期 $100.00 (+16.73%)
- 確定: 1968件 (Win 578 / Loss 749 / Flat 641) / pending 5件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000507 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EDEN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.73

## 6. Latest Market Context

- 更新: 2026-08-26T10:01:11.656179+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78385.7
- Funnel: target 1023 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +169.99% | $12,965,482.31 |
| BMT/USDT:USDT | +55.17% | $14,067,913.87 |
| TAC/USDT:USDT | +51.37% | $6,007,848.01 |
| LONGXIA/USDT:USDT | +28.91% | $1,966,663.84 |
| PORTAL/USDT:USDT | +20.76% | $3,900,809.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +0.66% | +0.70% |
| BEAT/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.45% | +0.49% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.44% | +0.48% |
| EDEN/USDT:USDT | below_1h_threshold | +0.43% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
