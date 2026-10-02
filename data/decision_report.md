# Decision Report

- generated_at: 2026-10-02T09:06:29.344537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15989**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15989, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.52% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.57% | **+0.28%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.35% | **+0.23%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.28% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,308.73** / 初期 $100.00 (+1208.73%)
- 確定: 6094件 (Win 1803 / Loss 1960 / Flat 2331) / skip 6456件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MANA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,308.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3604件 (Win 1005 / Loss 844 / Flat 1755) / skip 5796件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0304 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4148件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000079 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T09:06:17.869132+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=86200.1
- Funnel: target 1098 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +93.16% | $3,909,361.90 |
| SAND/USDT:USDT | +37.30% | $12,848,936.81 |
| MAGMA/USDT:USDT | +27.52% | $2,229,415.43 |
| CT/USDT:USDT | +27.00% | $8,350,697.63 |
| USELESS/USDT:USDT | +11.80% | $4,095,133.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUU/USDT:USDT | below_1h_threshold | +2.28% | +2.28% |
| BATON/USDT:USDT | below_1h_threshold | +1.17% | +1.18% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.12% |
| SOXL/USDT:USDT | below_1h_threshold | +1.10% | +1.11% |
| KORU/USDT:USDT | below_1h_threshold | +0.95% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
