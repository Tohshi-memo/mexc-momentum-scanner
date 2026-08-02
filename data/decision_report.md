# Decision Report

- generated_at: 2026-08-02T08:01:17.593225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10149**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10149, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/19 | 15.8% | +8.00% | **+1.26%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.05% | **+0.46%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.38% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$576.03** / 初期 $100.00 (+476.03%)
- 確定: 3668件 (Win 1166 / Loss 1201 / Flat 1301) / skip 3042件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $576.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2279件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0915 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.90** / 初期 $100.00 (+12.90%)
- 確定: 957件 (Win 305 / Loss 373 / Flat 279) / pending 4件 / skip 660件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.90

## 6. Latest Market Context

- 更新: 2026-08-02T08:01:10.408569+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63473.9
- Funnel: target 922 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +62.70% | $27,286,397.34 |
| BLESS/USDT:USDT | +43.64% | $10,257,280.94 |
| HOME/USDT:USDT | +37.58% | $2,066,574.92 |
| UAI/USDT:USDT | +30.90% | $23,116,502.67 |
| SATS/USDT:USDT | +10.78% | $1,011,957.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +0.89% | +0.88% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.52% | +0.51% |
| CAP/USDT:USDT | below_1h_threshold | +0.50% | +0.49% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
