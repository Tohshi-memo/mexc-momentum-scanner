# Decision Report

- generated_at: 2026-08-30T05:26:29.909901+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13024**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13024, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 12/17 | 70.6% | +1.52% | **+1.07%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.16% | **+0.41%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.22% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.50% | **+1.75%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.62% | **+1.05%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.45% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$789.14** / 初期 $100.00 (+689.14%)
- 確定: 4794件 (Win 1461 / Loss 1577 / Flat 1756) / skip 4791件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $789.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.04** / 初期 $100.00 (+74.04%)
- 確定: 2108件 (Win 590 / Loss 514 / Flat 1004) / skip 4327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0424 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $174.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 2067件 (Win 608 / Loss 802 / Flat 657) / pending 2件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-30T05:26:14.089144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78114.2
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +82.46% | $32,146,011.89 |
| NIULAI/USDT:USDT | +57.60% | $2,582,794.11 |
| FONE/USDT:USDT | +56.33% | $1,399,570.45 |
| PONS/USDT:USDT | +46.03% | $1,526,046.02 |
| PROM/USDT:USDT | +34.16% | $14,719,065.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.41% | +4.37% |
| BTR/USDT:USDT | below_1h_threshold | +3.69% | +3.65% |
| BTW/USDT:USDT | below_1h_threshold | +2.52% | +2.48% |
| TUT/USDT:USDT | below_1h_threshold | +2.35% | +2.31% |
| HNT/USDT:USDT | below_1h_threshold | +1.73% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
