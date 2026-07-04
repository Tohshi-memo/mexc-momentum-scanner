# Decision Report

- generated_at: 2026-07-04T07:25:06.512671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8231, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.50% | **-2.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.85% | **+0.18%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.13% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.27% | **+2.27%** |
| MARKET_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.57% | **+1.78%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.23% | **+1.69%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.60% | **+1.69%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$311.20** / 初期 $100.00 (+211.20%)
- 確定: 2548件 (Win 795 / Loss 849 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $311.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.45** / 初期 $100.00 (+7.45%)
- 確定: 627件 (Win 151 / Loss 151 / Flat 325) / skip 1015件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0979 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $107.45

## 5. Latest Market Context

- 更新: 2026-07-04T07:25:01.395399+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=62592.5
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +82.62% | $4,847,045.11 |
| TLM/USDT:USDT | +54.69% | $42,911,685.86 |
| HMSTR/USDT:USDT | +47.52% | $4,680,750.43 |
| VELVET/USDT:USDT | +46.29% | $27,445,523.30 |
| LAB/USDT:USDT | +41.97% | $50,179,453.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_relative_strength | +5.13% | +4.94% |
| GPS/USDT:USDT | below_1h_threshold | +3.06% | +2.87% |
| BSB/USDT:USDT | below_1h_threshold | +1.83% | +1.64% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.78% | +1.58% |
| BAS/USDT:USDT | below_1h_threshold | +1.52% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
